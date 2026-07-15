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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-78MS` (url=231ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=228ms, nekobox=263ms, status=yes)
3. `AKUN-003-PUBLICDOMAINREGISTRY-NET-VLESS-WS-81MS` (url=250ms, nekobox=246ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-86MS` (url=228ms, nekobox=249ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-90MS` (url=239ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS` (url=205ms, nekobox=248ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS` (url=231ms, nekobox=254ms, status=yes)
8. `AKUN-008-GO-DADDY-COM-LLC-VLESS-WS-87MS` (url=217ms, nekobox=236ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-102MS` (url=213ms, nekobox=239ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS` (url=205ms, nekobox=265ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=203ms, status=HTTP 204)
12. `AKUN-013-GO-DADDY-COM-LLC-VLESS-WS-116MS` (url=229ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-102MS` (url=222ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=226ms, status=HTTP 204)
15. `AKUN-016-466688-VLESS-WS-101MS` (url=217ms, status=HTTP 204)
16. `AKUN-017-WEBEX-VLESS-WS-79MS` (url=244ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-116MS` (url=247ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-93MS` (url=221ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-132MS` (url=271ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-122MS` (url=235ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-176MS` (url=228ms, status=HTTP 204)
22. `AKUN-023-NEXUSMODS-VLESS-WS-118MS` (url=245ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-235MS` (url=564ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-256MS` (url=1650ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-251MS` (url=575ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
