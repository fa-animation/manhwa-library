import { Box, Text, Flex } from '@chakra-ui/react'

import { GiChemicalDrop } from 'react-icons/gi'

function FloatingActionButton() {
  return (
    <Box
      position="fixed"
      zIndex={1}
      bottom="6"
      right="4"
      borderRadius="xl"
      bgGradient="linear-gradient(135deg, #007AFF, #00BFFF)"
      color="white"
      boxShadow="md"
      display="flex"
      py="1"
      px="2"
      justifyContent="center"
      alignItems="center"
      cursor="pointer"
    >
      <Flex alignItems={'center'} gap={2}>
        <GiChemicalDrop />
        <Text fontSize={{ base: 'xs', md: 'md' }}>Beta version</Text>
      </Flex>
    </Box>
  )
}

export default FloatingActionButton
