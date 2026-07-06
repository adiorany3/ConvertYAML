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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-117MS` (url=260ms, nekobox=297ms, status=yes)
2. `AKUN-002-OVH-VLESS-WS-123MS` (url=309ms, nekobox=306ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-125MS` (url=304ms, nekobox=319ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-124MS` (url=290ms, nekobox=337ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-128MS` (url=296ms, nekobox=221ms, status=no)
6. `AKUN-005-ZVC-VLESS-WS-101MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-125MS`
8. `AKUN-007-WPENG-VLESS-WS-117MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-128MS`
10. `AKUN-009-INTERNETWORKS-45-131-208-VLESS-WS-107MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-121MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-150MS` (url=273ms, status=HTTP 204)
13. `AKUN-013-WPENG-VLESS-WS-97MS` (url=345ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-145MS` (url=290ms, status=HTTP 204)
15. `AKUN-015-WEYRO-NET-VLESS-WS-167MS` (url=333ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-290MS` (url=732ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-332MS` (url=652ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-332MS` (url=815ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-337MS` (url=783ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-312MS` (url=799ms, status=HTTP 204)
21. `AKUN-022-WPENG-VLESS-WS-356MS` (url=634ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-361MS` (url=577ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-541MS` (url=859ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-641MS` (url=984ms, status=HTTP 204)
25. `AKUN-032-UNKNOWN-VLESS-WS-596MS` (url=1014ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
