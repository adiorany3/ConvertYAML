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
1. `AKUN-001-VULTR-VLESS-WS-66MS` (url=241ms, nekobox=257ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=231ms, nekobox=285ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=248ms, nekobox=270ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-78MS` (url=272ms, nekobox=266ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=239ms, nekobox=272ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=232ms, nekobox=274ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-97MS` (url=235ms, nekobox=272ms, status=yes)
8. `AKUN-008-NETCRAFTERS-VLESS-WS-105MS` (url=252ms, nekobox=299ms, status=yes)
9. `AKUN-009-COMPREND-NET-VLESS-WS-103MS` (url=258ms, nekobox=270ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-109MS` (url=274ms, nekobox=298ms, status=yes)
11. `AKUN-011-COMPREND-NET-VLESS-WS-106MS` (url=234ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-124MS` (url=231ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-253MS` (url=596ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-297MS` (url=655ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-277MS` (url=604ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-299MS` (url=647ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-306MS` (url=703ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-294MS` (url=639ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-289MS` (url=615ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-262MS` (url=556ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-349MS` (url=584ms, status=HTTP 204)
22. `AKUN-023-BIGCOMMERCE-VLESS-WS-475MS` (url=881ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-483MS` (url=739ms, status=HTTP 204)
24. `AKUN-026-RS-RAPIDSEEDBOX-20190717-VLESS-WS-521MS` (url=934ms, status=HTTP 204)
25. `AKUN-030-FASTCMD-VLESS-WS-573MS` (url=908ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
