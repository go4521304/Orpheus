// Fill out your copyright notice in the Description page of Project Settings.


#include "OrpheusController.h"
#include "InputMappingContext.h"
#include "InputAction.h"
#include "EnhancedInputSubsystems.h"
#include "EnhancedInputComponent.h"

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

	GetPawn()->AddMovementInput(asix, 1);

}