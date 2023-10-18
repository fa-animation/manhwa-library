import { Button as ChakraButton } from '@chakra-ui/react'

export const Button = () => (
  <ChakraButton
    width="100%"
    mt={{ base: '6', md: 0 }}
    color="black"
    _hover={{
      bg: 'gray.100'
    }}
    bg="gray.200"
    h="56px"
  >
    Browse Manhwa
  </ChakraButton>
)
