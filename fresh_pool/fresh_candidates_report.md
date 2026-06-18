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
1. `AKUN-001-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-68MS` (url=218ms, nekobox=256ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=224ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDWEBMANAGE-EU-FR-VLESS-WS-69MS` (url=222ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-74MS` (url=224ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS` (url=230ms, nekobox=235ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-78MS` (url=224ms, nekobox=260ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS` (url=239ms, nekobox=241ms, status=yes)
8. `AKUN-008-MYBB-VLESS-WS-82MS` (url=199ms, nekobox=248ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS`
10. `AKUN-011-CLOUDFLARE-VLESS-WS-99MS` (url=211ms, nekobox=181ms, status=no)
11. `AKUN-010-UNKNOWN-VLESS-WS-119MS`
12. `AKUN-013-OPENAI-VLESS-WS-122MS` (url=203ms, status=HTTP 204)
13. `AKUN-014-RS-RAPIDSEEDBOX-20190717-VLESS-WS-76MS` (url=222ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-70MS` (url=198ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-389MS` (url=889ms, status=HTTP 204)
16. `AKUN-018-CLOUDFLARE-VLESS-WS-70MS` (url=223ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-401MS` (url=800ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-392MS` (url=871ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-168MS` (url=367ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-390MS` (url=823ms, status=HTTP 204)
21. `AKUN-024-UNKNOWN-VLESS-WS-347MS` (url=738ms, status=HTTP 204)
22. `AKUN-025-CLOUDFLARE-VLESS-WS-405MS` (url=2594ms, status=HTTP 204)
23. `AKUN-034-FDCSERVERS-FRANKFURT2-VLESS-WS-772MS` (url=1395ms, status=HTTP 204)
24. `AKUN-035-CLOUDFLARE-VLESS-WS-838MS` (url=1277ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
