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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-69MS` (url=201ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS` (url=214ms, nekobox=240ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-82MS` (url=305ms, nekobox=229ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-80MS` (url=222ms, nekobox=248ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=215ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-90MS` (url=213ms, nekobox=244ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-83MS` (url=217ms, nekobox=246ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-86MS` (url=228ms, nekobox=255ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-91MS` (url=197ms, nekobox=227ms, status=yes)
10. `AKUN-010-466688-VLESS-WS-73MS` (url=222ms, nekobox=261ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-98MS` (url=232ms, status=HTTP 204)
12. `AKUN-012-CZ-LOTUNA-19970206-VLESS-WS-115MS` (url=203ms, status=HTTP 204)
13. `AKUN-013-DIXONS-VLESS-WS-110MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=227ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-121MS` (url=247ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-102MS` (url=231ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-135MS` (url=218ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-106MS` (url=208ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-123MS` (url=268ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-102MS` (url=225ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-116MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-UK-GB-DCL-01-20191003-VLESS-WS-116MS` (url=216ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-236MS` (url=752ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-235MS` (url=572ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-231MS` (url=513ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
