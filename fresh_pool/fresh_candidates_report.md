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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-66MS` (url=201ms, nekobox=238ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-62MS` (url=216ms, nekobox=236ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-64MS` (url=229ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=216ms, nekobox=255ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS` (url=231ms, nekobox=229ms, status=yes)
6. `AKUN-006-OVH-VLESS-WS-79MS` (url=235ms, nekobox=242ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-90MS` (url=200ms, nekobox=237ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-78MS` (url=199ms, nekobox=248ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-93MS` (url=221ms, nekobox=228ms, status=yes)
10. `AKUN-010-DIGITALOCEAN-VLESS-WS-85MS` (url=232ms, nekobox=265ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-91MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-105MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-ZVC-VLESS-WS-77MS` (url=225ms, status=HTTP 204)
14. `AKUN-014-WPENG-VLESS-WS-108MS` (url=201ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-110MS` (url=215ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-125MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-83MS` (url=221ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-74MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-83MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-75MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-90MS` (url=222ms, status=HTTP 204)
22. `AKUN-022-DEV-VLESS-WS-81MS` (url=208ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-103MS` (url=219ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-91MS` (url=215ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-374MS` (url=763ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
