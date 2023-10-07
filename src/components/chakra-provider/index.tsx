import { ChakraProvider as Chakra } from '@chakra-ui/react'

import customTheme from '@/styles/'

interface ChakraProps {
  children: React.ReactNode
}

export const ChakraProvider = ({ children }: ChakraProps) => {
  return <Chakra theme={customTheme}>{children}</Chakra>
}
