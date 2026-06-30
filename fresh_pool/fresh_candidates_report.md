# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 24
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-90MS` (url=233ms, nekobox=275ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-93MS` (url=213ms, nekobox=309ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-92MS` (url=231ms, nekobox=230ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-105MS` (url=227ms, nekobox=246ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-109MS` (url=227ms, nekobox=255ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=229ms, nekobox=229ms, status=yes)
7. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-98MS` (url=226ms, nekobox=228ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=207ms, nekobox=243ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-126MS` (url=212ms, nekobox=249ms, status=yes)
10. `AKUN-010-COMPREND-NET-VLESS-WS-124MS` (url=237ms, nekobox=245ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-100MS` (url=239ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-91MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-103MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-121MS` (url=202ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-128MS` (url=285ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-104MS` (url=220ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-238MS` (url=519ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-262MS` (url=2222ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-297MS` (url=627ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-302MS` (url=641ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-292MS` (url=620ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-398MS` (url=648ms, status=HTTP 204)
23. `AKUN-031-UNKNOWN-VLESS-WS-526MS` (url=920ms, status=HTTP 204)
24. `AKUN-034-UNKNOWN-VLESS-WS-547MS` (url=1006ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
