import { useColorModeValue } from '@chakra-ui/react'
import { IoIosAppstore } from 'react-icons/io'
import IconCard from '../Icon'
import { Heading, Text } from './typography'
import { BoxWrapper } from './box-wrapper'

export const CardItem = () => (
  <BoxWrapper bg={useColorModeValue('white', 'gray.600')}>
    <IconCard
      icon={IoIosAppstore}
      pos="absolute"
      left={0}
      right={0}
      justifyContent="center"
      marginInline="auto"
      top="-1.5rem"
    />
    <Heading color={useColorModeValue('#18216d', 'white')}>Easy and Quick</Heading>

    <Text color={useColorModeValue('#18216d', 'white')}>
      Get access to the book&#39;s You Purchase Online Instantly
    </Text>
  </BoxWrapper>
)
