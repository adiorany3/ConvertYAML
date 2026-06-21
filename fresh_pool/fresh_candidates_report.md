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
1. `AKUN-001-NET-NL-VLESS-WS-67MS` (url=200ms, nekobox=255ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS` (url=206ms, nekobox=234ms, status=yes)
3. `AKUN-003-NETCUP-VLESS-WS-65MS` (url=230ms, nekobox=250ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-67MS` (url=224ms, nekobox=224ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-71MS` (url=200ms, nekobox=239ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=231ms, nekobox=247ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-78MS` (url=224ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-64MS` (url=230ms, nekobox=248ms, status=yes)
9. `AKUN-009-VULTR-VLESS-WS-86MS` (url=216ms, nekobox=247ms, status=yes)
10. `AKUN-010-HOSTOFF-NET-VLESS-WS-71MS` (url=200ms, nekobox=230ms, status=yes)
11. `AKUN-011-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-MYBB-VLESS-WS-77MS` (url=228ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=224ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-72MS` (url=203ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-145MS` (url=227ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-74MS` (url=197ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-343MS` (url=779ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-354MS` (url=738ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-356MS` (url=782ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-382MS` (url=898ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-387MS` (url=860ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-402MS` (url=832ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-397MS` (url=853ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-97MS` (url=223ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
