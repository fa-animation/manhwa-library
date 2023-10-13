import { Flex, IconButton, Link, Text } from '@chakra-ui/react'
import { ImGithub } from 'react-icons/im'

const MyFooter = () => {
  return (
    <Flex mb={5} pos={'relative'} flexDir={'column'} w={'full'} alignItems={'center'} shadow="md">
      <Text fontSize={{ base: 'sm', md: 'md' }} fontWeight={'light'}>
        Manhwa Library 🌊
      </Text>
      <Text fontSize={{ base: 'sm', md: 'md' }} fontWeight={'light'}>
        Powered by Fã-animation
      </Text>
      <Flex py={2} gap={2}>
        <Link href="https://github.com/fa-animation" isExternal>
          <IconButton
            size={'sm'}
            colorScheme="gray"
            aria-label="Call Sage"
            fontSize="18px"
            icon={<ImGithub />}
          />
        </Link>
      </Flex>
    </Flex>
  )
}
export default MyFooter
