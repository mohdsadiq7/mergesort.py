#include<stdio.h>
int a[20][20],q[20],visited[20],r=-1,f=0,i,j,k,n,reach[20],indeg[20],flag[20],count=0;
void bfs(int v);
void dfs(int);
void tsort();
int main(){

    int v,count=0;
       printf("\nEnter no. of vertices:");
       scanf("%d",&n);
       for(i=1;i<=n;i++)
        {
         q[i]=0;
         visited[i]=0;
        }
       printf("\nEnter Adjacency Matrix of the graph:");
         for(i=1;i<=n;i++){
            for(j=1;j<=n;j++){
              printf("\nEnter a[%d][%d]:",i,j);
              scanf("%d",&a[i][j]);
              }
            }
         printf("\nEnter the node of ur Choice:");
         scanf("%d",&v);
         bfs(v);
         printf("\nAll the nodes reachable from node->%d is/are: ",v);
         for(i=1;i<=n;i++){
             if(visited[i])
                printf(" %d",i);
                }
         dfs(1);
         for(i=1;i<=n;i++)
         if(reach[i])
         count++;
         if(count==n)
         printf("Graph is connected\n");
         else
         printf("Graph is disconnected\n");
        count=0;
        tsort();
         return(0);
    }

    void bfs(int v)
	{
         for(i=1;i<=n;i++)
                if(a[v][i] && !visited[i])
                    q[++r]=i;
                if(f<=r){
                 visited[q[f]]=1;
                 bfs(q[f++]);
                 }
         }
void dfs(int v){
int i;
reach[v]=1;
for(i=1;i<=n;i++)
if(a[v][i]&&!reach[i])
{
printf("\n%d->%d",v,i);
dfs(i);
}
}
void tsort(){
    for(i=0;i<n;i++){
        indeg[i]=0;
        flag[i]=0;
    }

    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            indeg[i]=indeg[i]+a[j][i];

    printf("\nThe topological order is:");

    while(count<n){
        for(k=0;k<n;k++){
            if((indeg[k]==0) && (flag[k]==0)){
                printf("%d ",(k+1));
                flag [k]=1;
            }

            for(i=0;i<n;i++){
                if(a[i][k]==1)
                    indeg[k]--;
            }
        }

        count++;
    }

}
