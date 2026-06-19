# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 28

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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=240ms, nekobox=262ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=237ms, nekobox=267ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-67MS` (url=222ms, nekobox=188ms, status=no)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=265ms, nekobox=179ms, status=no)
5. `AKUN-003-CLOUDFLARE-VLESS-WS-76MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=203ms, nekobox=209ms, status=no)
7. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-70MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=207ms, nekobox=175ms, status=no)
10. `AKUN-006-CLOUDFLARE-VLESS-WS-83MS`
11. `AKUN-011-CLOUDFLARE-VLESS-WS-69MS` (url=251ms, nekobox=189ms, status=no)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-83MS` (url=249ms, nekobox=177ms, status=no)
13. `AKUN-007-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-100MS`
14. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-104MS`
15. `AKUN-015-SPEEDTEST-VLESS-WS-138MS` (url=374ms, nekobox=275ms, status=no)
16. `AKUN-009-UNKNOWN-VLESS-WS-377MS`
17. `AKUN-010-CLOUDFLARE-VLESS-WS-374MS`
18. `AKUN-018-UNKNOWN-VLESS-WS-413MS` (url=4548ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-403MS` (url=829ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-405MS` (url=832ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-438MS` (url=932ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-644MS` (url=925ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
