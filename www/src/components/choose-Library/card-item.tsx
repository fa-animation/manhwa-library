import { useColorModeValue } from '@chakra-ui/react'
import IconCard from '../Icon'
import { Heading, Text } from './typography'
import { BoxWrapper } from './box-wrapper'
import { BoosChoose } from './'

export const CardItem = ({ name, icon, description }: BoosChoose) => (
  <BoxWrapper bg={useColorModeValue('white', 'gray.600')}>
    <IconCard
      icon={icon}
      pos="absolute"
      left={0}
      right={0}
      justifyContent="center"
      marginInline="auto"
      top="-1.5rem"
      color={'white'}
    />
    <Heading color={useColorModeValue('#18216d', 'white')}>{name}</Heading>

    <Text color={useColorModeValue('#18216d', 'white')}>{description}</Text>
  </BoxWrapper>
)
