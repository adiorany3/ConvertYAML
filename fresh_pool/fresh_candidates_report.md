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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=210ms, nekobox=241ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-75MS` (url=202ms, nekobox=255ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-75MS` (url=211ms, nekobox=251ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-81MS` (url=206ms, nekobox=254ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-84MS` (url=249ms, nekobox=240ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=208ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=229ms, nekobox=7178ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-92MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-101MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-106MS`
12. `AKUN-012-242311-VLESS-WS-103MS` (url=267ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-97MS` (url=302ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-119MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-1PASSWORD-VLESS-WS-120MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-85MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-DIGITALOCEAN-VLESS-WS-92MS` (url=206ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, status=HTTP 204)
20. `AKUN-020-DEV-VLESS-WS-129MS` (url=200ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-104MS` (url=300ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-133MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-150MS` (url=226ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-140MS` (url=225ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-126MS` (url=219ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
