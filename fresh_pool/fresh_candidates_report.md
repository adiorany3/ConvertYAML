# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=216ms, nekobox=241ms, status=yes)
2. `AKUN-002-PUBLICDOMAINREGISTRY-NET-VLESS-WS-91MS` (url=241ms, nekobox=235ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-95MS` (url=232ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-94MS` (url=232ms, nekobox=237ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=311ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=216ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS` (url=227ms, nekobox=243ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-89MS` (url=212ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-104MS` (url=225ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-103MS` (url=251ms, nekobox=249ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=222ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-100MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-95MS` (url=247ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-138MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-WEBEX-VLESS-WS-119MS` (url=242ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-365MS` (url=756ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-376MS` (url=746ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-380MS` (url=785ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-413MS` (url=881ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-437MS` (url=820ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-355MS` (url=432ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-450MS` (url=1745ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-712MS` (url=1179ms, status=HTTP 204)
24. `AKUN-031-UNKNOWN-VLESS-WS-866MS` (url=1367ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-778MS` (url=1332ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
