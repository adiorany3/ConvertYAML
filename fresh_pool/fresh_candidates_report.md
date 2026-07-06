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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=214ms, nekobox=223ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=215ms, nekobox=255ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-68MS` (url=214ms, nekobox=258ms, status=yes)
4. `AKUN-004-WEBEX-VLESS-WS-83MS` (url=266ms, nekobox=231ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=210ms, nekobox=252ms, status=yes)
6. `AKUN-006-DIGITALOCEAN-VLESS-WS-79MS` (url=234ms, nekobox=262ms, status=yes)
7. `AKUN-007-WEYRO-NET-VLESS-WS-85MS` (url=224ms, nekobox=262ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-95MS` (url=210ms, nekobox=247ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-74MS` (url=218ms, nekobox=241ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-81MS` (url=220ms, nekobox=247ms, status=yes)
11. `AKUN-011-WEBEX-VLESS-WS-85MS` (url=227ms, status=HTTP 204)
12. `AKUN-012-466688-VLESS-WS-108MS` (url=214ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-120MS` (url=206ms, status=HTTP 204)
14. `AKUN-014-PAGES-VLESS-WS-125MS` (url=204ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-243MS` (url=504ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-241MS` (url=496ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-243MS` (url=528ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-107MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-259MS` (url=605ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-287MS` (url=594ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-284MS` (url=574ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-270MS` (url=646ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-428MS` (url=693ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-451MS` (url=745ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-296MS` (url=366ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
