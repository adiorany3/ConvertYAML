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
1. `AKUN-001-UNKNOWN-VLESS-WS-82MS` (url=255ms, nekobox=276ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-76MS` (url=228ms, nekobox=272ms, status=yes)
3. `AKUN-003-008500-VLESS-WS-78MS` (url=279ms, nekobox=269ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-77MS` (url=234ms, nekobox=262ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-99MS` (url=249ms, nekobox=293ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=284ms, nekobox=278ms, status=yes)
7. `AKUN-007-DEV-VLESS-WS-95MS` (url=270ms, nekobox=204ms, status=no)
8. `AKUN-007-UNKNOWN-VLESS-WS-82MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-97MS`
10. `AKUN-010-DEV-VLESS-WS-84MS` (url=246ms, nekobox=189ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-123MS`
12. `AKUN-012-DEV-VLESS-WS-104MS` (url=263ms, nekobox=188ms, status=no)
13. `AKUN-010-CLOUDFLARE-VLESS-WS-270MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-299MS` (url=643ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-298MS` (url=652ms, status=HTTP 204)
16. `AKUN-016-WPENG-VLESS-WS-312MS` (url=5412ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-309MS` (url=620ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-292MS` (url=2200ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-295MS` (url=617ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-289MS` (url=2266ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-468MS` (url=750ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-451MS` (url=665ms, status=HTTP 204)
23. `AKUN-033-CLOUDFLARE-VLESS-WS-582MS` (url=947ms, status=HTTP 204)
24. `AKUN-034-CLOUDFLARE-VLESS-WS-605MS` (url=1157ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
