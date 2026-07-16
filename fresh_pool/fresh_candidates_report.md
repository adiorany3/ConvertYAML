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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=201ms, nekobox=250ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-68MS` (url=218ms, nekobox=239ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=217ms, nekobox=234ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-65MS` (url=208ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-68MS` (url=228ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=212ms, nekobox=233ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-72MS` (url=242ms, nekobox=256ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-80MS` (url=224ms, nekobox=237ms, status=yes)
9. `AKUN-009-GO-DADDY-COM-LLC-VLESS-WS-107MS` (url=209ms, nekobox=260ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-117MS` (url=226ms, nekobox=262ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-101MS` (url=207ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-105MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-POLICE-VLESS-WS-116MS` (url=276ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-117MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-129MS` (url=230ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-100MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-109MS` (url=198ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-100MS` (url=200ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-123MS` (url=213ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-177MS` (url=225ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-238MS` (url=550ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-239MS` (url=527ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-236MS` (url=521ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-255MS` (url=3812ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-250MS` (url=495ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
