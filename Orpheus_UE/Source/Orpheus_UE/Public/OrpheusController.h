// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/PlayerController.h"
#include "InputActionValue.h"
#include "OrpheusController.generated.h"


/**
 *
 */
UCLASS()
class ORPHEUS_UE_API AOrpheusController : public APlayerController
{
	GENERATED_BODY()

public:
	AOrpheusController();

	/** MappingContext */
	UPROPERTY(VisibleAnywhere, Category = Input)
	class UInputMappingContext* DefaultMappingContext;

	UPROPERTY(VisibleAnywhere, Category = Input)
	class UInputAction* EquipAction;


protected:
	virtual void SetupInputComponent() override;
	virtual void BeginPlay();

	void Move(const FInputActionValue& Value);

	class AMapPlatform* Platform;

	uint8 curRow = 0, curCol = 0;
};
