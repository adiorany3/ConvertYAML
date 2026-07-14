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
1. `AKUN-001-UNKNOWN-VLESS-WS-61MS` (url=218ms, nekobox=230ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-64MS` (url=219ms, nekobox=254ms, status=yes)
3. `AKUN-003-466688-VLESS-WS-67MS` (url=230ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-64MS` (url=215ms, nekobox=255ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-79MS` (url=228ms, nekobox=7177ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-72MS`
7. `AKUN-006-IDC-SG-VLESS-WS-89MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-74MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-70MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-70MS` (url=209ms, nekobox=229ms, status=yes)
11. `AKUN-010-CLOUDFLARE-VLESS-WS-119MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-96MS` (url=206ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-116MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-91MS` (url=206ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-137MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-111MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-NOAGUO-VLESS-WS-148MS` (url=305ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-133MS` (url=226ms, status=HTTP 204)
19. `AKUN-019-WEBEX-VLESS-WS-86MS` (url=201ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-108MS` (url=245ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-144MS` (url=218ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-79MS` (url=231ms, status=HTTP 204)
23. `AKUN-023-PUBLICDOMAINREGISTRY-NET-VLESS-WS-69MS` (url=194ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-359MS` (url=818ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-376MS` (url=726ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
