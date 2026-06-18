# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 21
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 27

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
1. `AKUN-001-090227-VLESS-WS-136MS` (url=302ms, nekobox=293ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-143MS` (url=252ms, nekobox=232ms, status=no)
3. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-138MS`
4. `AKUN-003-CLOUDFLARE-VLESS-WS-147MS`
5. `AKUN-005-UNKNOWN-VLESS-WS-138MS` (url=245ms, nekobox=227ms, status=no)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-150MS` (url=254ms, nekobox=233ms, status=no)
7. `AKUN-004-CLOUDFLARE-VLESS-WS-138MS`
8. `AKUN-005-CLOUDFLARE-VLESS-WS-149MS`
9. `AKUN-009-DEV-VLESS-WS-161MS` (url=273ms, nekobox=234ms, status=no)
10. `AKUN-006-OPENAI-VLESS-WS-163MS`
11. `AKUN-007-UNKNOWN-VLESS-WS-164MS`
12. `AKUN-008-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-167MS`
13. `AKUN-015-CLOUDFLARE-VLESS-WS-401MS` (url=3320ms, nekobox=503ms, status=no)
14. `AKUN-009-RS-RAPIDSEEDBOX-20190717-VLESS-WS-393MS`
15. `AKUN-010-CLOUDFLARE-VLESS-WS-423MS`
16. `AKUN-019-CLOUDFLARE-VLESS-WS-409MS` (url=754ms, status=HTTP 204)
17. `AKUN-020-CLOUDFLARE-VLESS-WS-519MS` (url=842ms, status=HTTP 204)
18. `AKUN-022-ARAD-VLESS-WS-501MS` (url=816ms, status=HTTP 204)
19. `AKUN-023-CLOUDFLARE-VLESS-WS-558MS` (url=906ms, status=HTTP 204)
20. `AKUN-028-UNKNOWN-VLESS-WS-637MS` (url=1025ms, status=HTTP 204)
21. `AKUN-029-CLOUDFLARE-VLESS-WS-630MS` (url=1007ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
