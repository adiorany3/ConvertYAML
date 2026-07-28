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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=220ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-74MS`
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS`
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-96MS`
5. `AKUN-006-CLOUDFLARE-VLESS-WS-99MS` (url=211ms, nekobox=173ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-78MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-71MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-71MS`
9. `AKUN-010-CLOUDFLARE-VLESS-WS-73MS` (url=223ms, nekobox=171ms, status=no)
10. `AKUN-008-CLOUDFLARE-VLESS-WS-73MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-93MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-90MS`
13. `AKUN-014-CLOUDFLARE-VLESS-WS-83MS` (url=216ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-108MS` (url=221ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-125MS` (url=215ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-86MS` (url=213ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-102MS` (url=239ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-105MS` (url=216ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-58MS` (url=215ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-120MS` (url=278ms, status=HTTP 204)
21. `AKUN-022-090227-VLESS-WS-268MS` (url=576ms, status=HTTP 204)
22. `AKUN-024-CONFLU-VLESS-WS-354MS` (url=728ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-662MS` (url=1075ms, status=HTTP 204)
24. `AKUN-030-CLOUDFLARE-VLESS-WS-667MS` (url=3846ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-775MS` (url=1246ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
