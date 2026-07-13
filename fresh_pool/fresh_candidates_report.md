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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=220ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=224ms, nekobox=229ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-86MS` (url=206ms, nekobox=237ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=215ms, nekobox=243ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-115MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-104MS`
8. `AKUN-008-UNKNOWN-VLESS-WS-111MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-115MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-74MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-98MS` (url=235ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-124MS` (url=202ms, status=HTTP 204)
13. `AKUN-014-466688-VLESS-WS-100MS` (url=226ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-104MS` (url=219ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-157MS` (url=233ms, status=HTTP 204)
16. `AKUN-017-GO-DADDY-COM-LLC-VLESS-WS-79MS` (url=232ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-134MS` (url=213ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-139MS` (url=218ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-236MS` (url=495ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-237MS` (url=2016ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-277MS` (url=561ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-247MS` (url=558ms, status=HTTP 204)
23. `AKUN-024-INTERNETWORKS-45-131-208-VLESS-WS-280MS` (url=1057ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-300MS` (url=386ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-463MS` (url=713ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
