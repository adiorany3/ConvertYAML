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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=213ms, nekobox=239ms, status=yes)
2. `AKUN-002-090227-VLESS-WS-61MS` (url=210ms, nekobox=249ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=205ms, nekobox=242ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-58MS` (url=226ms, nekobox=229ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=198ms, nekobox=234ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-97MS` (url=218ms, nekobox=253ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-95MS` (url=209ms, nekobox=235ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-62MS` (url=211ms, nekobox=238ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-96MS` (url=224ms, nekobox=7176ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-85MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-78MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-113MS` (url=210ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-70MS` (url=218ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=221ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-115MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-97MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-73MS` (url=209ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-99MS` (url=250ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-110MS` (url=212ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-125MS` (url=217ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-142MS` (url=313ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-79MS` (url=392ms, status=HTTP 204)
23. `AKUN-023-WPENG-VLESS-WS-155MS` (url=225ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-130MS` (url=197ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-353MS` (url=777ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
