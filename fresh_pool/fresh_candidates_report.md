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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=232ms, nekobox=263ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-71MS` (url=228ms, nekobox=258ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=247ms, nekobox=274ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-68MS` (url=251ms, nekobox=271ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS` (url=231ms, nekobox=266ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-73MS` (url=235ms, nekobox=261ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-83MS` (url=233ms, nekobox=270ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-72MS` (url=230ms, nekobox=278ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-59MS` (url=229ms, nekobox=266ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=249ms, nekobox=275ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=249ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-78MS` (url=247ms, status=HTTP 204)
13. `AKUN-013-CZ-LOTUNA-19970206-VLESS-WS-80MS` (url=285ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-73MS` (url=234ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-74MS` (url=231ms, status=HTTP 204)
16. `AKUN-016-SHOPIFY-VLESS-WS-88MS` (url=241ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-68MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-DEV-VLESS-WS-86MS` (url=224ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-92MS` (url=230ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-75MS` (url=233ms, status=HTTP 204)
21. `AKUN-021-1PASSWORD-VLESS-WS-79MS` (url=294ms, status=HTTP 204)
22. `AKUN-022-NEXUSMODS-VLESS-WS-97MS` (url=272ms, status=HTTP 204)
23. `AKUN-023-ORG-VLESS-WS-74MS` (url=237ms, status=HTTP 204)
24. `AKUN-024-MEDIUM-VLESS-WS-84MS` (url=248ms, status=HTTP 204)
25. `AKUN-025-466688-VLESS-WS-85MS` (url=278ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
