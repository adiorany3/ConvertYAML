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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-57MS` (url=198ms, nekobox=229ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-56MS` (url=199ms, nekobox=225ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-59MS` (url=204ms, nekobox=225ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-61MS` (url=203ms, nekobox=234ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-62MS` (url=200ms, nekobox=226ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-70MS` (url=199ms, nekobox=223ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-80MS` (url=199ms, nekobox=227ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-72MS` (url=203ms, nekobox=228ms, status=yes)
9. `AKUN-009-EU-VLESS-WS-77MS` (url=197ms, nekobox=234ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-82MS` (url=209ms, nekobox=230ms, status=yes)
11. `AKUN-011-DEV-VLESS-WS-73MS` (url=208ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-67MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-100MS` (url=201ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=225ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-105MS` (url=206ms, status=HTTP 204)
16. `AKUN-016-008500-VLESS-WS-88MS` (url=204ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-72MS` (url=200ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-59MS` (url=220ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-115MS` (url=211ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-129MS` (url=199ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-66MS` (url=205ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-95MS` (url=224ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-68MS` (url=207ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-138MS` (url=198ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-114MS` (url=225ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
