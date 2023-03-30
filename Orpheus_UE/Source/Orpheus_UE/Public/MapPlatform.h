// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "MapPlatform.generated.h"

UCLASS()
class ORPHEUS_UE_API AMapPlatform : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AMapPlatform();

	// 바닥 세팅
	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Platform Setting", meta = (DisplayName = "행 개수", ClampMin = 1))
	uint8 rowNum = 1;

	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "Platform Setting", meta = (DisplayName = "열 개수", ClampMin = 1))
	uint8 colNum = 1;

	UFUNCTION(BlueprintImplementableEvent)
	FVector GetPosition(uint8 row, uint8 col);

protected:
	UPROPERTY(EditAnywhere, BlueprintReadOnly)
	class UStaticMeshComponent* StaticMeshComponent;

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called every frame
	virtual void Tick(float DeltaTime) override;
};
