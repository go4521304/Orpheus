// Fill out your copyright notice in the Description page of Project Settings.


#include "MapPlatform.h"
#include "Components/StaticMeshComponent.h"
#include "Engine/StaticMeshActor.h"
#include "Engine/EngineTypes.h"

// Sets default values
AMapPlatform::AMapPlatform()
{
 //	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	//PrimaryActorTick.bCanEverTick = true;
	////SetRootComponent(nullptr);

	//StaticMeshComponent = CreateDefaultSubobject<UStaticMeshComponent>("TEST");
	//static ConstructorHelpers::FObjectFinder<UStaticMesh> StaticMesh(TEXT("/Script/Engine.StaticMesh'/Game/Platform/Basic_Map.Basic_Map'"));
	//if (StaticMesh.Succeeded())
	//{
	//	//StaticMeshComponent->SetStaticMesh(StaticMesh.Object);
	//	//StaticMeshComponent->SetWorldRotation(FRotator(0, -90, 0).Quaternion());
	//	StaticMeshComponent->SetStaticMesh(StaticMesh.Object);
	//}

	//static ConstructorHelpers::FObjectFinder<UStaticMesh> mesh(TEXT("/Script/Engine.StaticMesh'/Engine/BasicShapes/Sphere.Sphere'"));
	//pointMesh = mesh.Object;
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

//void AMapPlatform::OnConstruction(const FTransform& Transform)
//{
//	/*Super::OnConstruction(Transform);
//
//	UStaticMeshComponent* newOne = NewObject<UStaticMeshComponent>(this); 
//	newOne->SetStaticMesh(StaticMeshComponent->GetStaticMesh());
//	newOne->AttachToComponent(GetRootComponent(), FAttachmentTransformRules::KeepRelativeTransform);*/
//
//	//StaticMeshComponent->AttachToComponent(GetRootComponent(), FAttachmentTransformRules::KeepRelativeTransform);
//
//	//StaticMeshComponent->SetMaterial(0, Material);
//	//UE_LOG(LogTemp, Log, TEXT("%s"), *StaticMeshComponent->Bounds.Origin.ToString());
//	//FVector s_point = StaticMeshComponent->Bounds.Origin - StaticMeshComponent->Bounds.BoxExtent;
//	//s_point.Z = StaticMeshComponent->Bounds.Origin.Z + 25.0f;
//	//int rowBound = (StaticMeshComponent->Bounds.BoxExtent.X) * 2 / rowNum, colBound = (StaticMeshComponent->Bounds.BoxExtent.Y) * 2 / colNum;
//	//s_point.X += (rowBound / 2);
//	//s_point.Y += (colBound / 2);
//
//	//for (AActor* i : points)
//	//{
//	//	i->Destroy();
//	//}
//
//	//points.Empty();
//
//	//// 수정 해야함
//	//for (int i = 0; i < rowNum; ++i)
//	//{
//	//	FVector temp_point = s_point;
//	//	for (int j = 0; j < colNum; ++j)
//	//	{	
//	//		UChildActorComponent* NewComp1 = NewObject<UChildActorComponent>(this);
//	//		NewComp1->bEditableWhenInherited = true;
//	//		NewComp1->RegisterComponent();
//	//		NewComp1->SetChildActorClass(AStaticMeshActor::StaticClass());
//	//		NewComp1->CreateChildActor();
//	//		reinterpret_cast<AStaticMeshActor*>(NewComp1->GetChildActor())->GetStaticMeshComponent()->SetStaticMesh(pointMesh);
//	//		NewComp1->GetChildActor()->SetActorScale3D(FVector(0.5f, 0.5f, 0.5f));
//	//		NewComp1->GetChildActor()->SetActorLocation(temp_point);
//	//		
//	//		points.Add(NewComp1->GetChildActor());
//
//	//		temp_point.Y += colBound;
//	//	}
//	//	s_point.X += rowBound;
//	//}
//}
