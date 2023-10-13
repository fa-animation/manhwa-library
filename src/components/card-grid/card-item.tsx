import { Box, Heading, Text, useColorModeValue } from '@chakra-ui/react'
import { IoIosAppstore } from 'react-icons/io'
import IconCard from '../Icon'

export const CardItem = () => (
  <Box
    pos="relative"
    rounded="12px"
    shadow="base"
    p="40px"
    bg={useColorModeValue('white', 'gray.600')}
  >
    <IconCard
      icon={IoIosAppstore}
      pos="absolute"
      left={0}
      right={0}
      justifyContent="center"
      marginInline="auto"
      top="-1.5rem"
    />
    <Heading
      as="h3"
      size="md"
      fontWeight="semibold"
      mt="1em"
      mb="0.5em"
      textAlign={'center'}
      color={useColorModeValue('#18216d', 'white')}
    >
      Easy and Quick
    </Heading>
    <Text
      fontSize="lg"
      opacity={0.7}
      color={useColorModeValue('#18216d', 'white')}
      textAlign={'center'}
    >
      Get access to the book&#39;s You Purchase Online Instantly
    </Text>
  </Box>
)
