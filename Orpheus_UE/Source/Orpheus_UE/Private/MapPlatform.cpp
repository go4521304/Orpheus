// Fill out your copyright notice in the Description page of Project Settings.


#include "MapPlatform.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/StaticMeshActor.h"
#include "Engine/EngineTypes.h"

// Sets default values
AMapPlatform::AMapPlatform()
{
	PrimaryActorTick.bCanEverTick = true;
	StaticMeshComponent = CreateDefaultSubobject<UStaticMeshComponent>("Mesh");
	static ConstructorHelpers::FObjectFinder<UStaticMesh> StaticMesh(TEXT("/Script/Engine.StaticMesh'/Game/Platform/Basic_Map.Basic_Map'"));
	if (StaticMesh.Succeeded())
	{
		StaticMeshComponent->SetStaticMesh(StaticMesh.Object);
	}
}

// Called when the game starts or when spawned
void AMapPlatform::BeginPlay()
{
	Super::BeginPlay();
}

// Called every frame
void AMapPlatform::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}