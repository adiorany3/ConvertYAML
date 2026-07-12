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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-77MS` (url=201ms, nekobox=234ms, status=yes)
2. `AKUN-002-ALIBABA-VLESS-WS-82MS` (url=212ms, nekobox=267ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-80MS` (url=202ms, nekobox=279ms, status=yes)
4. `AKUN-004-466688-VLESS-WS-85MS` (url=200ms, nekobox=308ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-91MS` (url=224ms, nekobox=226ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-93MS` (url=223ms, nekobox=264ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-101MS` (url=230ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-81MS` (url=204ms, nekobox=233ms, status=yes)
9. `AKUN-009-466688-VLESS-WS-103MS` (url=206ms, nekobox=243ms, status=yes)
10. `AKUN-010-877774-VLESS-WS-115MS` (url=231ms, nekobox=255ms, status=yes)
11. `AKUN-011-NET-82-21-84-0-24-VLESS-WS-116MS` (url=226ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-85MS` (url=208ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-101MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-119MS` (url=239ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=222ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-83MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-129MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-US-VLESS-WS-96MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-NOTION-WEB-VLESS-WS-106MS` (url=240ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-129MS` (url=265ms, status=HTTP 204)
21. `AKUN-021-PUBLICDOMAINREGISTRY-NET-VLESS-WS-73MS` (url=200ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-161MS` (url=238ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-118MS` (url=237ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-368MS` (url=1477ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-370MS` (url=4786ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
