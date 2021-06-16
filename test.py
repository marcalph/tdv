self.arr_convblock = [ConvBlock(outdim, outdim) for _ in range(number_convblock)]
self.arr_convblock[0] = ConvBlock(indim, outdim)