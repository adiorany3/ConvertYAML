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
1. `AKUN-001-UNKNOWN-VLESS-WS-60MS` (url=217ms, nekobox=243ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, nekobox=285ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-65MS` (url=210ms, nekobox=249ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-69MS` (url=220ms, nekobox=267ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-58MS` (url=213ms, nekobox=266ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-72MS` (url=232ms, nekobox=251ms, status=yes)
7. `AKUN-007-OVH-VLESS-WS-78MS` (url=243ms, nekobox=258ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=210ms, nekobox=242ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-83MS` (url=224ms, nekobox=7179ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-70MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-66MS`
12. `AKUN-012-1PASSWORD-VLESS-WS-81MS` (url=234ms, status=HTTP 204)
13. `AKUN-013-UDACITY-VLESS-WS-82MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-67MS` (url=223ms, status=HTTP 204)
15. `AKUN-015-MEDIUM-VLESS-WS-80MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-79MS` (url=222ms, status=HTTP 204)
17. `AKUN-017-MYBB-VLESS-WS-70MS` (url=232ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-85MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-SHOPIFY-VLESS-WS-82MS` (url=258ms, status=HTTP 204)
20. `AKUN-020-ADF-VLESS-WS-109MS` (url=226ms, status=HTTP 204)
21. `AKUN-021-DEV-VLESS-WS-126MS` (url=227ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-75MS` (url=221ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-94MS` (url=230ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-209MS` (url=254ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-330MS` (url=750ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
