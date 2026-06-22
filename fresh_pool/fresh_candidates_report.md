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
1. `AKUN-001-AMBYRE-NET-VLESS-WS-73MS` (url=218ms, nekobox=249ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-75MS` (url=232ms, nekobox=203ms, status=no)
3. `AKUN-002-CLOUDFLARE-VLESS-WS-69MS`
4. `AKUN-003-008500-VLESS-WS-76MS`
5. `AKUN-004-DIGITALOCEAN-VLESS-WS-78MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-76MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-87MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-86MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-114MS`
10. `AKUN-009-OPENAI-VLESS-WS-122MS`
11. `AKUN-010-CLOUDWEBMANAGE-EU-FR-VLESS-WS-71MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-121MS` (url=230ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-109MS` (url=211ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-87MS` (url=243ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-80MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-EU-VLESS-WS-102MS` (url=235ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-91MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-116MS` (url=227ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-124MS` (url=257ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-78MS` (url=204ms, status=HTTP 204)
21. `AKUN-021-1PASSWORD-VLESS-WS-95MS` (url=211ms, status=HTTP 204)
22. `AKUN-022-MYBB-VLESS-WS-79MS` (url=232ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-357MS` (url=736ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-383MS` (url=824ms, status=HTTP 204)
25. `AKUN-025-SPEEDTEST-VLESS-WS-389MS` (url=799ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
