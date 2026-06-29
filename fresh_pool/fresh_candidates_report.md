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
1. `AKUN-001-UNKNOWN-VLESS-WS-109MS` (url=282ms, nekobox=353ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-136MS` (url=292ms, nekobox=329ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-117MS` (url=291ms, nekobox=207ms, status=no)
4. `AKUN-003-COMPREND-NET-VLESS-WS-116MS`
5. `AKUN-004-UNKNOWN-VLESS-WS-131MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-130MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-130MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-131MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-150MS`
10. `AKUN-009-COMPREND-NET-VLESS-WS-143MS`
11. `AKUN-010-RS-RAPIDSEEDBOX-20190717-VLESS-WS-152MS`
12. `AKUN-012-COMPREND-NET-VLESS-WS-133MS` (url=289ms, status=HTTP 204)
13. `AKUN-013-COMPREND-NET-VLESS-WS-162MS` (url=273ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-149MS` (url=262ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-234MS` (url=303ms, status=HTTP 204)
16. `AKUN-017-WPENG-VLESS-WS-128MS` (url=318ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-313MS` (url=609ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-356MS` (url=674ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-316MS` (url=703ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-138MS` (url=369ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-377MS` (url=752ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-386MS` (url=688ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-312MS` (url=639ms, status=HTTP 204)
24. `AKUN-029-RS-RAPIDSEEDBOX-20190717-VLESS-WS-617MS` (url=1016ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-620MS` (url=1207ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
