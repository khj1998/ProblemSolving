#include <iostream>
#include <string>
#include <utility>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
using namespace std;

int INF = INT_MAX;
int R, C;
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };
int jihun_map[1000][1000];
int fire_map[1000][1000];
string graph[1000];
vector<pair<int, int>> start;
vector<pair<int, int>> f_start;

void init_array()
{
	for (int i = 0; i <= R-1; i++)
		for (int j = 0; j <= C-1; j++)
			jihun_map[i][j] = INF;

	for (int i = 0; i <= R-1; i++)
		for (int j = 0; j <= C-1; j++)
			fire_map[i][j] = INF;

}

void input()
{
	cin >> R >> C;
	init_array();

	for (int i = 0; i <= R-1; i++)
		cin >> graph[i];

	for (int i = 0; i <= R-1; i++)
		for (int j = 0; j <= C-1; j++)
		{
			if (graph[i][j] == 'J')
				start.push_back(make_pair(i, j));
			else if (graph[i][j] == 'F')
				f_start.push_back(make_pair(i,j));
		}
}

void jihun_bfs()
{
	queue<pair<int,int>> q;
	int start1 = start.front().first;
	int start2 = start.front().second;
	q.push(make_pair(start1,start2));
	jihun_map[start1][start2] = 1;
	
	while (!q.empty())
	{
		int x = q.front().first;
		int y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int px = x + dx[i];
			int py = y + dy[i];

			if (0<= px && px<=R-1 && 0 <= py &&py<=C-1)
				if ((jihun_map[px][py] > jihun_map[x][y] + 1) && graph[px][py] == '.')
				{
					jihun_map[px][py] = jihun_map[x][y] + 1;
					q.push(make_pair(px,py));
				}
		}
	}
}

void fire_bfs()
{
	queue<pair<int, int>> q;
	int x, y = 0;
	
	for (int i = 0; i < f_start.size(); i++)
	{
		x = f_start[i].first;
		y = f_start[i].second;
		fire_map[x][y] = 1;
		q.push(make_pair(x,y));
	}

	while (!q.empty())
	{
		x = q.front().first;
		y = q.front().second;
		q.pop();
		for (int i = 0; i < 4; i++)
		{
			int px = x + dx[i];
			int py = y + dy[i];

			if (0 <= px && px <= R - 1 && 0 <= py && py <= C - 1)
				if ((fire_map[px][py] > fire_map[x][y] + 1) && graph[px][py] == '.')
				{
					fire_map[px][py] = fire_map[x][y] + 1;
					q.push(make_pair(px, py));
				}
		}
	}
}

void solution()
{
	int ans = INF;
	jihun_bfs();
	fire_bfs();

	for (int i = 0; i <= C-1; i++)
		if (jihun_map[0][i] < fire_map[0][i])
			ans = min(ans,jihun_map[0][i]);

	for (int i = 0; i <= C-1; i++)
		if (jihun_map[R-1][i] < fire_map[R-1][i])
			ans = min(ans, jihun_map[R-1][i]);

	for (int i = 0; i <= R-1; i++)
		if (jihun_map[i][0] < fire_map[i][0])
			ans = min(ans, jihun_map[i][0]);

	for (int i = 0; i <= R-1; i++)
		if (jihun_map[i][C-1] < fire_map[i][C-1])
			ans = min(ans, jihun_map[i][C-1]);

	if (ans == INF)
		printf("IMPOSSIBLE");
	else
		printf("%d", ans);
}

int main(void)
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	input();
	solution();
	return 0;
}