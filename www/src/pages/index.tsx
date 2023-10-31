import type { GetStaticProps } from 'next'
import Head from 'next/head'
import HeroPage from '@/containers/HeroPage'
import CardGrid from '@/components/card-grid'
import Explore from '@/components/explore'
import LastCard from '@/components/last-grids'
import api from '@/api/'
import { ArrayDataProps } from '@/types'

export const getStaticProps: GetStaticProps = async (context: any) => {
  try {
    const { data: lastHomeManga } = await api.get('/v1/manga/?order_by=created_at&limit=5')
    return {
      props: {
        lastHomeManga
      },
      revalidate: 60000
    }
  } catch (error) {
    return {
      notFound: true
    }
  }
}

export default function Home({ lastHomeManga }: ArrayDataProps) {
  return (
    <>
      <Head>
        <title>Manga Library</title>
      </Head>
      <HeroPage />
      <CardGrid />
      <LastCard lastHomeManga={lastHomeManga} />
      <Explore />
    </>
  )
}
