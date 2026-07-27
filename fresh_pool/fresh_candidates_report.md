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
1. `AKUN-001-UNKNOWN-VLESS-WS-54MS` (url=223ms, nekobox=263ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-55MS` (url=212ms, nekobox=245ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-54MS` (url=220ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-65MS` (url=229ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-67MS` (url=222ms, nekobox=247ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-68MS` (url=220ms, nekobox=235ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=209ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-71MS` (url=215ms, nekobox=242ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-60MS` (url=212ms, nekobox=234ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-84MS` (url=210ms, nekobox=239ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-ZVC-VLESS-WS-61MS` (url=197ms, status=HTTP 204)
13. `AKUN-013-SKK-VLESS-WS-71MS` (url=194ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-93MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-83MS` (url=214ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-98MS` (url=225ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-102MS` (url=261ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-90MS` (url=211ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-95MS` (url=232ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-109MS` (url=233ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-95MS` (url=223ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-91MS` (url=213ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-111MS` (url=281ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-340MS` (url=6704ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-395MS` (url=3300ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
