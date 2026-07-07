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
1. `AKUN-001-UNKNOWN-VLESS-WS-91MS` (url=300ms, nekobox=311ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-106MS` (url=257ms, nekobox=274ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-103MS` (url=300ms, nekobox=281ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-127MS` (url=276ms, nekobox=331ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-131MS` (url=262ms, nekobox=339ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-101MS` (url=292ms, nekobox=223ms, status=no)
7. `AKUN-006-DEV-VLESS-WS-132MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-130MS`
9. `AKUN-008-ZVC-VLESS-WS-96MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-137MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS`
12. `AKUN-012-OVH-VLESS-WS-142MS` (url=294ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-131MS` (url=255ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-93MS` (url=284ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-124MS` (url=228ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-143MS` (url=285ms, status=HTTP 204)
17. `AKUN-017-WPENG-VLESS-WS-96MS` (url=256ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-129MS` (url=298ms, status=HTTP 204)
19. `AKUN-019-ES-FORNEX-20160629-VLESS-WS-157MS` (url=270ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-242MS` (url=468ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-302MS` (url=717ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-319MS` (url=694ms, status=HTTP 204)
23. `AKUN-024-GALAKTIKA-20201015-VLESS-WS-300MS` (url=748ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-304MS` (url=593ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-302MS` (url=879ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
