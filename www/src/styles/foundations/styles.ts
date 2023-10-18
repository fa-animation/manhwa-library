import type { DeepPartial, Theme } from '@chakra-ui/react'

export const styles: DeepPartial<Theme['styles']> = {
  global: {
    'body::-webkit-scrollbar': {
      width: '5px'
    },
    'body::-webkit-scrollbar-track': {
      background: 'black'
    },
    'body::-webkit-scrollbar-thumb': {
      background: '#4FD1C5',
      borderRadius: '3px'
    },
    'body::-webkit-scrollbar-thumb:hover': {
      background: '#4FD1C5'
    }
  }
}
