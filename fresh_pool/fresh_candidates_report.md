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
1. `AKUN-001-1PASSWORD-VLESS-WS-85MS` (url=232ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=234ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=229ms, nekobox=247ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-93MS` (url=204ms, nekobox=232ms, status=yes)
5. `AKUN-005-GO-DADDY-COM-LLC-VLESS-WS-93MS` (url=231ms, nekobox=231ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=222ms, nekobox=263ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-101MS` (url=226ms, nekobox=258ms, status=yes)
8. `AKUN-008-UK-GB-DCL-01-20191003-VLESS-WS-110MS` (url=220ms, nekobox=260ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=206ms, nekobox=239ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS` (url=236ms, nekobox=262ms, status=yes)
11. `AKUN-011-466688-VLESS-WS-105MS` (url=235ms, status=HTTP 204)
12. `AKUN-012-UK-GB-DCL-01-20191003-VLESS-WS-117MS` (url=213ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-118MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-111MS` (url=232ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-95MS` (url=235ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-101MS` (url=201ms, status=HTTP 204)
17. `AKUN-017-DEV-VLESS-WS-103MS` (url=211ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-106MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-104MS` (url=235ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-90MS` (url=203ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-155MS` (url=207ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-102MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-100MS` (url=200ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-135MS` (url=228ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-122MS` (url=857ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
