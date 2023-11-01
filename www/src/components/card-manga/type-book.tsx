import { Text, TextProps } from '@chakra-ui/react'

interface TypeBookProps extends TextProps {
  type: string
}

export const TypeBook = ({ type, ...props }: TypeBookProps) => (
  <Text
    position="absolute"
    top="4"
    right="4"
    bg={'purple.700'}
    p={2}
    rounded={'base'}
    fontWeight={'bold'}
    fontSize={'10px'}
    cursor={'pointer'}
    color={'white'}
    {...props}
  >
    {type}
  </Text>
)
