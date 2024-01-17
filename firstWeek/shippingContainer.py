numWidgets = 1234567

smallContainer = 1
mediumContainer = 5
largeContainer = 20
hugeContainer = 50


hugeContainerCount = numWidgets//hugeContainer

numWidgets = numWidgets - (hugeContainer * hugeContainerCount)

largeContainerCount = numWidgets//largeContainer

numWidgets = numWidgets - (largeContainer * largeContainerCount)

mediumContainerCount = numWidgets//mediumContainer

numWidgets = numWidgets - (mediumContainer * mediumContainerCount)

smallContainerCount = numWidgets//smallContainer

numWidgets = numWidgets - (smallContainer * smallContainerCount)

print("you need {} Huge Containers, {} Large Containers, {} medium containers, {} small Containers"
      .format(hugeContainerCount, largeContainerCount, mediumContainerCount, smallContainerCount))