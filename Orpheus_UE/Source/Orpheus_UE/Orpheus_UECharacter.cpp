// Copyright Epic Games, Inc. All Rights Reserved.

#include "Orpheus_UECharacter.h"
#include "UObject/ConstructorHelpers.h"
#include "Camera/CameraComponent.h"
#include "Components/DecalComponent.h"
#include "Components/CapsuleComponent.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/SpringArmComponent.h"
#include "Materials/Material.h"
#include "Engine/World.h"
#include "PaperFlipBook.h"
#include "PaperFlipbookComponent.h"

AOrpheus_UECharacter::AOrpheus_UECharacter()
{
	SetActorScale3D(FVector(0.7f, 0.7f, 0.7f));

	// Set size for player capsule
	GetCapsuleComponent()->InitCapsuleSize(42.f, 96.0f);

	// Don't rotate character to camera direction
	bUseControllerRotationPitch = false;
	bUseControllerRotationYaw = false;
	bUseControllerRotationRoll = false;

	// Configure character movement
	GetCharacterMovement()->bOrientRotationToMovement = true; // Rotate character to moving direction
	GetCharacterMovement()->RotationRate = FRotator(0.f, 640.f, 0.f);
	GetCharacterMovement()->bConstrainToPlane = true;
	GetCharacterMovement()->bSnapToPlaneAtStart = true;
	GetCharacterMovement()->RotationRate = FRotator(0.f, 0.f, 0.f);

	// Create a camera boom...
	CameraBoom = CreateDefaultSubobject<USpringArmComponent>(TEXT("CameraBoom"));
	CameraBoom->SetupAttachment(RootComponent);
	CameraBoom->SetUsingAbsoluteRotation(true); // Don't want arm to rotate when character does
	CameraBoom->TargetArmLength = 400.f;
	CameraBoom->SetRelativeLocation(FVector(200.f, 0.f, 0.f));
	CameraBoom->SetRelativeRotation(FRotator(-10.f, -90.f, 0.f));
	CameraBoom->bDoCollisionTest = false; // Don't want to pull camera in when it collides with level

	// Create a camera...
	TopDownCameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("TopDownCamera"));
	TopDownCameraComponent->SetupAttachment(CameraBoom, USpringArmComponent::SocketName);
	TopDownCameraComponent->bUsePawnControlRotation = false; // Camera does not rotate relative to arm

	// Activate ticking in order to update the cursor every frame.
	PrimaryActorTick.bCanEverTick = true;
	PrimaryActorTick.bStartWithTickEnabled = true;

	GetMesh()->SetVisibility(false);

	Sprite = CreateDefaultSubobject<UPaperFlipbookComponent>(TEXT("Sprite"));
	Sprite->SetupAttachment(GetCapsuleComponent());
	Sprite->SetWorldScale3D(FVector(0.1f, 0.1f, 0.1f));

	static ConstructorHelpers::FObjectFinder<UPaperFlipbook> defaultSprite(TEXT("/Script/Paper2D.PaperFlipbook'/Game/Characters/Sprite/Orpheus_RD.Orpheus_RD'"));
	
	if (defaultSprite.Succeeded())
		Sprite->SetFlipbook(defaultSprite.Object);

}

void AOrpheus_UECharacter::Tick(float DeltaSeconds)
{
    Super::Tick(DeltaSeconds);
}
