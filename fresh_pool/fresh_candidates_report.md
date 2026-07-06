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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-60MS` (url=220ms, nekobox=234ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-57MS` (url=226ms, nekobox=253ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-71MS` (url=215ms, nekobox=243ms, status=yes)
4. `AKUN-004-DIGITALOCEAN-VLESS-WS-67MS` (url=221ms, nekobox=257ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-66MS` (url=204ms, nekobox=253ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS` (url=215ms, nekobox=246ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-71MS` (url=228ms, nekobox=226ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-65MS` (url=225ms, nekobox=244ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS` (url=213ms, nekobox=257ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-80MS` (url=225ms, nekobox=227ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-62MS` (url=203ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-76MS` (url=204ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-74MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-76MS` (url=207ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-87MS` (url=227ms, status=HTTP 204)
16. `AKUN-016-WEYRO-NET-VLESS-WS-81MS` (url=234ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-107MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=232ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-88MS` (url=313ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-112MS` (url=211ms, status=HTTP 204)
21. `AKUN-021-WPENG-VLESS-WS-67MS` (url=204ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-86MS` (url=293ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-352MS` (url=766ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-377MS` (url=856ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-388MS` (url=811ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
