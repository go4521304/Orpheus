// Copyright Epic Games, Inc. All Rights Reserved.

#include "Orpheus_UEGameMode.h"
#include "Orpheus_UEPlayerController.h"
#include "Orpheus_UECharacter.h"
#include "UObject/ConstructorHelpers.h"

AOrpheus_UEGameMode::AOrpheus_UEGameMode()
{
	// use our custom PlayerController class
	PlayerControllerClass = AOrpheus_UEPlayerController::StaticClass();

	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/TopDown/Blueprints/BP_TopDownCharacter"));
	if (PlayerPawnBPClass.Class != nullptr)
	{
		DefaultPawnClass = PlayerPawnBPClass.Class;
	}

	// set default controller to our Blueprinted controller
	static ConstructorHelpers::FClassFinder<APlayerController> PlayerControllerBPClass(TEXT("/Script/CoreUObject.Class'/Script/Orpheus_UE.OrpheusController'"));
	if(PlayerControllerBPClass.Class != NULL)
	{
		PlayerControllerClass = PlayerControllerBPClass.Class;
	}
}