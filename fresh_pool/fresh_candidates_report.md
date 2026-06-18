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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-93MS` (url=223ms, nekobox=202ms, status=no)
2. `AKUN-001-CNAE-VLESS-WS-104MS`
3. `AKUN-003-DEV-VLESS-WS-120MS` (url=235ms, nekobox=193ms, status=no)
4. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-97MS`
5. `AKUN-003-CLOUDFLARE-VLESS-WS-122MS`
6. `AKUN-004-UNKNOWN-VLESS-WS-121MS`
7. `AKUN-007-DEV-VLESS-WS-130MS` (url=231ms, nekobox=219ms, status=no)
8. `AKUN-005-OPENAI-VLESS-WS-125MS`
9. `AKUN-006-CLOUDFLARE-VLESS-WS-119MS`
10. `AKUN-007-CLOUDFLARE-VLESS-WS-129MS`
11. `AKUN-008-CLOUDFLARE-VLESS-WS-118MS`
12. `AKUN-009-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-104MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-138MS` (url=230ms, nekobox=217ms, status=no)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-297MS` (url=2729ms, nekobox=421ms, status=no)
15. `AKUN-010-CLOUDFLARE-VLESS-WS-285MS`
16. `AKUN-016-UNKNOWN-VLESS-WS-290MS` (url=633ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-298MS` (url=610ms, status=HTTP 204)
18. `AKUN-019-ARAD-VLESS-WS-407MS` (url=627ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-400MS` (url=682ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-498MS` (url=923ms, status=HTTP 204)
21. `AKUN-028-CLOUDFLARE-VLESS-WS-421MS` (url=696ms, status=HTTP 204)
22. `AKUN-029-CLOUDFLARE-VLESS-WS-585MS` (url=949ms, status=HTTP 204)
23. `AKUN-030-UNKNOWN-VLESS-WS-542MS` (url=878ms, status=HTTP 204)
24. `AKUN-033-UNKNOWN-VLESS-WS-667MS` (url=4087ms, status=HTTP 204)
25. `AKUN-035-CLOUDFLARE-VLESS-WS-645MS` (url=2332ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
