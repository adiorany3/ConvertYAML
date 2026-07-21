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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-169MS` (url=341ms, nekobox=368ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-172MS` (url=787ms, nekobox=360ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-179MS` (url=1385ms, nekobox=405ms, status=yes)
4. `AKUN-004-ZOOM-VLESS-WS-186MS` (url=399ms, nekobox=375ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-195MS` (url=533ms, nekobox=380ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-181MS` (url=332ms, nekobox=375ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-204MS` (url=357ms, nekobox=391ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-192MS` (url=322ms, nekobox=361ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-208MS` (url=739ms, nekobox=418ms, status=yes)
10. `AKUN-010-OVH-VLESS-WS-212MS` (url=327ms, nekobox=701ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-201MS` (url=337ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-238MS` (url=386ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-206MS` (url=1835ms, status=HTTP 204)
14. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-324MS` (url=582ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-202MS` (url=302ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-465MS` (url=949ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-452MS` (url=928ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-484MS` (url=2832ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-491MS` (url=4216ms, status=HTTP 204)
20. `AKUN-020-ORG-VLESS-WS-280MS` (url=343ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-704MS` (url=821ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-812MS` (url=1543ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-569MS` (url=5620ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-807MS` (url=1297ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
