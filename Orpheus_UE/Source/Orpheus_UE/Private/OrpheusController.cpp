// Fill out your copyright notice in the Description page of Project Settings.


#include "OrpheusController.h"
#include "InputMappingContext.h"
#include "InputAction.h"
#include "EnhancedInputSubsystems.h"
#include "EnhancedInputComponent.h"
#include "EngineUtils.h"
#include "MapPlatform.h"

AOrpheusController::AOrpheusController()
{
	static ConstructorHelpers::FObjectFinder<UInputMappingContext> IMC_Orp(TEXT("/Script/EnhancedInput.InputMappingContext'/Game/Control/Input/IMC_Orpheus.IMC_Orpheus'"));
	if (IMC_Orp.Succeeded())
	{
		DefaultMappingContext = IMC_Orp.Object;
	}

	static ConstructorHelpers::FObjectFinder<UInputAction> IA_Move(TEXT("/Script/EnhancedInput.InputAction'/Game/Control/Input/IA_Move.IA_Move'"));
	if (IA_Move.Succeeded())
	{
		EquipAction = IA_Move.Object;
	}
}

void AOrpheusController::BeginPlay()
{
	// Call the base class  
	Super::BeginPlay();

	//Add Input Mapping Context
	if (UEnhancedInputLocalPlayerSubsystem* Subsystem = ULocalPlayer::GetSubsystem<UEnhancedInputLocalPlayerSubsystem>(GetLocalPlayer()))
	{
		Subsystem->AddMappingContext(DefaultMappingContext, 0);
	}

	for (const auto& it : TActorRange<AMapPlatform>(GetWorld()))
	{
		Platform = it;
	}
	FVector pos = Platform->GetPosition(curRow, curCol);
	pos.Z = GetPawn()->GetActorLocation().Z;
	GetPawn()->SetActorLocation(pos);
}

void AOrpheusController::SetupInputComponent()
{
	Super::SetupInputComponent();

	if (UEnhancedInputComponent* EnhancedInputComponent = Cast<UEnhancedInputComponent>(InputComponent))
	{
		EnhancedInputComponent->BindAction(EquipAction, ETriggerEvent::Triggered, this, &AOrpheusController::Move);
	}
}


void AOrpheusController::Move(const FInputActionValue& Value)
{
	FVector asix = Value.Get<FVector>();

	UE_LOG(LogTemp, Log, TEXT("Input Action: %s"), *asix.ToString());

	uint8 tempRow = curRow + asix.Y, tempCol = curCol + asix.X;

	curRow += asix.Y;
	curCol += asix.X;

	FVector pos = Platform->GetPosition(curRow, curCol);

	pos.Z = GetPawn()->GetActorLocation().Z;
	GetPawn()->SetActorLocation(pos);

	UE_LOG(LogTemp, Log, TEXT("Row: %d, Col: %d"), curRow, curCol);
}