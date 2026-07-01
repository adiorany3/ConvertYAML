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
1. `AKUN-001-VULTR-VLESS-WS-65MS` (url=210ms, nekobox=240ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-81MS` (url=212ms, nekobox=232ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS` (url=216ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-77MS` (url=212ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=224ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-81MS` (url=207ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-96MS` (url=253ms, nekobox=234ms, status=yes)
8. `AKUN-008-COMPREND-NET-VLESS-WS-88MS` (url=212ms, nekobox=259ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-109MS` (url=220ms, nekobox=341ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-87MS` (url=224ms, nekobox=243ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-97MS` (url=205ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-112MS` (url=225ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-69MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-88MS` (url=231ms, status=HTTP 204)
15. `AKUN-015-OVH-VLESS-WS-113MS` (url=217ms, status=HTTP 204)
16. `AKUN-016-AEZA-NETWORK-VLESS-WS-115MS` (url=200ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-123MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-COMPREND-NET-VLESS-WS-111MS` (url=221ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-238MS` (url=563ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-245MS` (url=500ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-253MS` (url=489ms, status=HTTP 204)
22. `AKUN-024-ZOOM-VLESS-WS-96MS` (url=229ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-270MS` (url=598ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-265MS` (url=589ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-265MS` (url=582ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
